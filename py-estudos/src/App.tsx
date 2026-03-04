import React, { useEffect, useState, useCallback, useMemo } from 'react';
import Sidebar from './components/Sidebar';
import NotebookReader from './components/NotebookReader';
import QuizPanel from './components/QuizPanel';
import StatsPanel from './components/StatsPanel';
import PythonSandbox from './components/PythonSandbox';
import type { Challenge } from './components/PythonSandbox';
import {
  MODULES, QUIZZES, loadProgress, saveProgress, getModulesWithProgress,
} from './data';
import { fetchNotebook } from './utils/notebook';
import type { Notebook, Progress } from './types';
import './App.css';

type PanelView = 'quiz' | 'stats' | 'sandbox';

// Map module IDs to Mimo challenge file prefixes (01_desafio_*.py → module 01, etc.)
const CHALLENGE_MAP: Record<string, string[]> = {
  '01': ['01_desafio_1.py', '01_desafio_2.py', '01_desafio_3.py'],
  '02': ['02_desafio_1.py', '02_desafio_2.py', '02_desafio_3.py'],
  '03': ['03_desafio_1.py', '03_desafio_2.py', '03_desafio_3.py'],
  '04': ['04_desafio_1.py', '04_desafio_2.py', '04_desafio_3.py'],
  '05': ['05_desafio_1.py', '05_desafio_2.py', '05_desafio_3.py'],
  '06': ['06_desafio_1.py', '06_desafio_2.py', '06_desafio_3.py'],
  '07': ['07_desafio_1.py', '07_desafio_2.py', '07_desafio_3.py'],
  '08': ['08_desafio_1.py', '08_desafio_2.py', '08_desafio_3.py'],
  '09': ['09_desafio_1.py', '09_desafio_2.py', '09_desafio_3.py'],
  '10': ['10_desafio_1.py', '10_desafio_2.py', '10_desafio_3.py'],
  '11': ['11_desafio_1.py', '11_desafio_2.py', '11_desafio_3.py'],
  '12': ['12_desafio_1.py', '12_desafio_2.py', '12_desafio_3.py'],
  '13': ['13_desafio_1.py', '13_desafio_2.py', '13_desafio_3.py'],
  '14': ['14_desafio_1.py', '14_desafio_2.py', '14_desafio_3.py'],
};

async function loadChallenges(moduleId: string): Promise<Challenge[]> {
  const files = CHALLENGE_MAP[moduleId] ?? [];
  const results: Challenge[] = [];
  for (const filename of files) {
    try {
      const res = await fetch(`/desafios/${filename}`);
      if (!res.ok) continue;
      const text = await res.text();
      // Extract description from first comment lines
      const lines = text.split('\n');
      const commentLines = lines
        .filter(l => l.trim().startsWith('#'))
        .map(l => l.replace(/^#\s*/, '').trim())
        .filter(l => l.length > 0);
      const description = commentLines.slice(1).join(' ').substring(0, 200) || 'Pratique o código deste desafio.';
      const num = filename.replace(/[^0-9]/g, '').slice(-1); // last digit = 1,2,3
      results.push({
        filename,
        title: `Desafio ${num}`,
        description,
        code: text,
      });
    } catch { /* skip */ }
  }
  return results;
}

const App: React.FC = () => {
  const [progress, setProgress] = useState<Progress>(loadProgress);
  const [activeId, setActiveId] = useState<string>('01');
  const [notebook, setNotebook] = useState<Notebook | null>(null);
  const [loading, setLoading] = useState(false);
  const [panelView, setPanelView] = useState<PanelView>('quiz');
  const [challenges, setChallenges] = useState<Challenge[]>([]);

  const modules = useMemo(() => getModulesWithProgress(progress), [progress]);
  const activeModule = modules.find(m => m.id === activeId)!;
  const activeIndex = modules.findIndex(m => m.id === activeId);

  const loadModule = useCallback(async (id: string) => {
    const mod = MODULES.find(m => m.id === id);
    if (!mod) return;
    setLoading(true);
    setNotebook(null);
    const nb = await fetchNotebook(mod.filename);
    setNotebook(nb);
    setLoading(false);
    // Load challenges for this module
    const ch = await loadChallenges(id);
    setChallenges(ch);
    // Update streak / weekly progress
    setProgress(prev => {
      const today = new Date().getDay();
      const newWeekly = [...prev.weeklyProgress];
      newWeekly[today] = (newWeekly[today] || 0) + 1;
      const updated = { ...prev, lastVisited: new Date().toISOString(), weeklyProgress: newWeekly };
      saveProgress(updated);
      return updated;
    });
  }, []);

  useEffect(() => { loadModule(activeId); }, [activeId, loadModule]);

  const handleSelect = (id: string) => {
    setActiveId(id);
    setPanelView('quiz');
  };

  const handleComplete = () => {
    if (progress.completedModules.includes(activeId)) return;
    const updated: Progress = {
      ...progress,
      completedModules: [...progress.completedModules, activeId],
    };
    setProgress(updated);
    saveProgress(updated);
  };

  // Redo: remove module from completed so it goes back to "current"
  const handleRedo = () => {
    const updated: Progress = {
      ...progress,
      completedModules: progress.completedModules.filter(id => id !== activeId),
      quizScores: Object.fromEntries(
        Object.entries(progress.quizScores).filter(([id]) => id !== activeId)
      ),
    };
    setProgress(updated);
    saveProgress(updated);
  };

  const handleQuizScore = (score: number) => {
    const updated: Progress = {
      ...progress,
      quizScores: { ...progress.quizScores, [activeId]: score },
    };
    setProgress(updated);
    saveProgress(updated);
  };

  const handlePrev = () => {
    const prev = modules[activeIndex - 1];
    if (prev && prev.status !== 'locked') setActiveId(prev.id);
  };

  const handleNext = () => {
    const next = modules[activeIndex + 1];
    if (next && next.status !== 'locked') setActiveId(next.id);
    else if (next) {
      handleComplete();
      setActiveId(next.id);
    }
  };

  const completedCount = progress.completedModules.length;
  const quizzes = QUIZZES[activeId] ?? [];

  return (
    <div className="app">
      <Sidebar
        modules={modules}
        activeId={activeId}
        onSelect={handleSelect}
        completedCount={completedCount}
      />

      <main className="main">
        <NotebookReader
          notebook={notebook}
          loading={loading}
          moduleTitle={activeModule?.title ?? ''}
          moduleNumber={activeModule?.number ?? 1}
          totalModules={modules.length}
          onComplete={handleComplete}
          onRedo={handleRedo}
          onPrev={handlePrev}
          onNext={handleNext}
          hasPrev={activeIndex > 0}
          hasNext={activeIndex < modules.length - 1}
          isCompleted={progress.completedModules.includes(activeId)}
        />
      </main>

      <aside className="right-panel">
        <div className="right-tabs">
          <button
            className={`right-tab ${panelView === 'quiz' ? 'active' : ''}`}
            onClick={() => setPanelView('quiz')}
          >
            📝 Quiz
          </button>
          <button
            className={`right-tab ${panelView === 'sandbox' ? 'active' : ''}`}
            onClick={() => setPanelView('sandbox')}
          >
            ⚡ Sandbox
          </button>
          <button
            className={`right-tab ${panelView === 'stats' ? 'active' : ''}`}
            onClick={() => setPanelView('stats')}
          >
            📊 Stats
          </button>
        </div>
        <div className="right-content">
          {panelView === 'quiz' && (
            <QuizPanel
              key={activeId}
              moduleId={activeId}
              quizzes={quizzes}
              onScore={handleQuizScore}
              savedScore={progress.quizScores[activeId]}
            />
          )}
          {panelView === 'sandbox' && (
            <PythonSandbox
              key={activeId}
              notebook={notebook}
              moduleTitle={activeModule?.title ?? ''}
              moduleId={activeId}
              challenges={challenges}
            />
          )}
          {panelView === 'stats' && (
            <StatsPanel progress={progress} totalModules={modules.length} />
          )}
        </div>
      </aside>
    </div>
  );
};

export default App;
