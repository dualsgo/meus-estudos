import React from 'react';
import type { Progress } from '../types';
import './StatsPanel.css';

interface StatsPanelProps {
  progress: Progress;
  totalModules: number;
}

const DAYS = ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'];

const StatsPanel: React.FC<StatsPanelProps> = ({ progress, totalModules }) => {
  const pct = Math.round((progress.completedModules.length / totalModules) * 100);
  const maxWeekly = Math.max(...progress.weeklyProgress, 1);
  const today = new Date().getDay();

  return (
    <div className="stats-panel">
      <div className="stats-card">
        <div className="stats-card-header">
          <span className="stats-icon">📊</span>
          <span className="stats-label">Progresso Geral</span>
          <span className="stats-pct-badge">{pct}%</span>
        </div>
        <div className="stats-bar-bg">
          <div className="stats-bar-fill" style={{ width: `${pct}%` }} />
        </div>
        <p className="stats-sub">{progress.completedModules.length} de {totalModules} módulos concluídos</p>
      </div>

      <div className="stats-card streak-card">
        <div className="stats-card-header">
          <span className="stats-icon">🔥</span>
          <span className="stats-label">Sequência</span>
        </div>
        <div className="streak-display">
          <span className="streak-num">{progress.streak}</span>
          <span className="streak-label">dias seguidos</span>
        </div>
        <div className="week-dots">
          {DAYS.map((d, i) => (
            <div key={i} className={`week-day ${i === today ? 'today' : i < today ? 'done' : ''}`}>
              <div className="week-dot" />
              <span className="week-letter">{d}</span>
            </div>
          ))}
        </div>
      </div>

      <div className="stats-card">
        <div className="stats-card-header">
          <span className="stats-icon">📈</span>
          <span className="stats-label">Atividade Semanal</span>
        </div>
        <div className="weekly-bars">
          {progress.weeklyProgress.map((val, i) => (
            <div key={i} className="weekly-bar-wrap">
              <div
                className={`weekly-bar ${i === today ? 'today-bar' : ''}`}
                style={{ height: `${(val / maxWeekly) * 52}px` }}
                title={`${val} lições`}
              />
              <span className="weekly-bar-label">{DAYS[i]}</span>
            </div>
          ))}
        </div>
      </div>

      <div className="stats-card">
        <div className="stats-card-header">
          <span className="stats-icon">🏆</span>
          <span className="stats-label">Conquistas</span>
        </div>
        <div className="achievements">
          {progress.completedModules.length >= 1 && (
            <div className="badge-chip earned" title="Primeiro módulo!">🌱 Iniciante</div>
          )}
          {progress.completedModules.length >= 5 && (
            <div className="badge-chip earned" title="5 módulos!">⚡ Dedicado</div>
          )}
          {progress.completedModules.length >= 10 && (
            <div className="badge-chip earned" title="10 módulos!">🔥 Persistente</div>
          )}
          {progress.streak >= 7 && (
            <div className="badge-chip earned" title="1 semana de streak!">📅 Semanal</div>
          )}
          {progress.completedModules.length >= 20 && (
            <div className="badge-chip earned" title="Todos os módulos!">🏆 Mestre Python</div>
          )}
          {Object.values(progress.quizScores).filter(s => s >= 80).length >= 3 && (
            <div className="badge-chip earned" title="3 quizzes com nota ≥80!">⭐ Estudioso</div>
          )}
          {progress.completedModules.length < 1 && (
            <p className="no-badges">Complete módulos para ganhar conquistas!</p>
          )}
        </div>
      </div>

      <div className="quick-links">
        <p className="stats-label" style={{ marginBottom: 8 }}>🔗 Recursos</p>
        <a href="https://docs.python.org/3/" target="_blank" rel="noreferrer" className="res-link">
          📚 Docs oficiais Python
        </a>
        <a href="https://peps.python.org/pep-0008/" target="_blank" rel="noreferrer" className="res-link">
          📐 PEP 8 — Guia de estilo
        </a>
        <a href="https://www.python.org/shell/" target="_blank" rel="noreferrer" className="res-link">
          ▶ Python Online Shell
        </a>
      </div>
    </div>
  );
};

export default StatsPanel;
