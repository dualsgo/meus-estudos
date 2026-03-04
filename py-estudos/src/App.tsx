import React, { useEffect, useState, useCallback } from 'react';
import Sidebar from './components/Sidebar';
import NotebookReader from './components/NotebookReader';
import QuizPanel from './components/QuizPanel';
import StatsPanel from './components/StatsPanel';
import PythonSandbox from './components/PythonSandbox';
import {
  MODULES, QUIZZES, loadProgress, saveProgress, getModulesWithProgress,
} from './data';
import { fetchNotebook } from './utils/notebook';
import type { Notebook, Progress } from './types';
import './App.css';

type PanelView = 'quiz' | 'stats' | 'sandbox';

const App: React.FC = () => {
  const [progress, setProgress] = useState<Progress>(loadProgress);
  const [activeId, setActiveId] = useState<string>('01');
  const [notebook, setNotebook] = useState<Notebook | null>(null);
  const [loading, setLoading] = useState(false);
  const [panelView, setPanelView] = useState<PanelView>('quiz');

  const modules = getModulesWithProgress(progress);
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
      // Unlock next after completing current
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
              notebook={notebook}
              moduleTitle={activeModule?.title ?? ''}
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
