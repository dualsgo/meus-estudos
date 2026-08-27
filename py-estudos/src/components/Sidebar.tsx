import React from 'react';
import type { Module } from '../types';
import './Sidebar.css';

interface SidebarProps {
  modules: Module[];
  activeId: string;
  onSelect: (id: string) => void;
  completedCount: number;
}

const statusIcon = (status: Module['status'], score?: number) => {
  if (status === 'completed') {
    return (
      <span className="status-icon completed" title={score !== undefined ? `Quiz: ${score}%` : 'Concluído'}>
        {score !== undefined && score >= 80 ? '⭐' : '✓'}
      </span>
    );
  }
  if (status === 'current') return <span className="status-icon current">▶</span>;
  return <span className="status-icon locked">🔒</span>;
};

const Sidebar: React.FC<SidebarProps> = ({ modules, activeId, onSelect, completedCount }) => {
  const progressPct = Math.round((completedCount / modules.length) * 100);

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <div className="logo">
          <span className="logo-icon">🐍</span>
          <div>
            <h1 className="logo-title">PyEstudos</h1>
            <p className="logo-sub">Seus Resumos</p>
          </div>
        </div>
      </div>

      <div className="progress-overview">
        <div className="progress-label">
          <span>Progresso Geral</span>
          <span className="progress-pct">{progressPct}%</span>
        </div>
        <div className="progress-bar-bg">
          <div className="progress-bar-fill" style={{ width: `${progressPct}%` }} />
        </div>
        <span className="progress-count">{completedCount} de {modules.length} módulos</span>
      </div>

      <nav className="module-list">
        <p className="nav-label">SYLLABUS · {modules.length} módulos</p>
        {modules.map(mod => (
          <button
            key={mod.id}
            className={`module-item ${mod.status} ${activeId === mod.id ? 'active' : ''}`}
            onClick={() => mod.status !== 'locked' && onSelect(mod.id)}
            disabled={mod.status === 'locked'}
          >
            <span className="module-num">{String(mod.number).padStart(2, '0')}</span>
            <span className="module-title">{mod.title}</span>
            {statusIcon(mod.status, mod.quizScore)}
          </button>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;
