import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import hljs from 'highlight.js/lib/core';
import python from 'highlight.js/lib/languages/python';
import 'highlight.js/styles/github-dark.css';
import type { Notebook } from '../types';
import { getCellSource } from '../utils/notebook';
import './NotebookReader.css';

hljs.registerLanguage('python', python);

interface NotebookReaderProps {
  notebook: Notebook | null;
  loading: boolean;
  moduleTitle: string;
  moduleNumber: number;
  totalModules: number;
  onComplete: () => void;
  onRedo: () => void;
  onPrev: () => void;
  onNext: () => void;
  hasPrev: boolean;
  hasNext: boolean;
  isCompleted: boolean;
}

const CodeBlock: React.FC<{ code: string; output?: string[] }> = ({ code, output }) => {
  const [copied, setCopied] = useState(false);
  const highlighted = hljs.highlight(code, { language: 'python' }).value;

  const copy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="code-block">
      <div className="code-header">
        <div className="code-dots">
          <span className="dot red" />
          <span className="dot yellow" />
          <span className="dot green" />
        </div>
        <span className="code-lang">Python</span>
        <button className="copy-btn" onClick={copy}>
          {copied ? '✓ Copiado!' : '⧉ Copiar'}
        </button>
      </div>
      <pre className="code-pre">
        <code
          className="hljs language-python"
          dangerouslySetInnerHTML={{ __html: highlighted }}
        />
      </pre>
      {output && output.length > 0 && (
        <div className="code-output">
          <span className="output-label">▶ Saída:</span>
          <pre className="output-pre">{output.join('')}</pre>
        </div>
      )}
    </div>
  );
};

const NotebookReader: React.FC<NotebookReaderProps> = ({
  notebook, loading, moduleTitle, moduleNumber, totalModules,
  onComplete, onRedo, onPrev, onNext, hasPrev, hasNext, isCompleted,
}) => {
  const [readPct, setReadPct] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      const el = document.querySelector('.content-scroll');
      if (!el) return;
      const pct = Math.min(100, Math.round((el.scrollTop / (el.scrollHeight - el.clientHeight)) * 100));
      setReadPct(isNaN(pct) ? 0 : pct);
    };
    const el = document.querySelector('.content-scroll');
    el?.addEventListener('scroll', handleScroll);
    return () => el?.removeEventListener('scroll', handleScroll);
  }, [notebook]);

  useEffect(() => { setReadPct(0); }, [notebook]);

  if (loading) {
    return (
      <div className="reader-loading">
        <div className="snake-loader">🐍</div>
        <p>Carregando módulo...</p>
      </div>
    );
  }

  if (!notebook) {
    return (
      <div className="reader-empty">
        <span>📂</span>
        <p>Selecione um módulo para começar</p>
      </div>
    );
  }

  return (
    <div className="reader">
      <div className="reader-topbar">
        <div className="reader-breadcrumb">
          <span className="bc-home">Módulos</span>
          <span className="bc-sep">›</span>
          <span className="bc-current">{String(moduleNumber).padStart(2, '0')}: {moduleTitle}</span>
        </div>
        <div className="reader-badge-row">
          <span className={`module-badge ${isCompleted ? 'badge-done' : 'badge-progress'}`}>
            {isCompleted ? '✓ CONCLUÍDO' : '▶ EM PROGRESSO'}
          </span>
          <span className="module-position">MÓDULO {moduleNumber} DE {totalModules}</span>
        </div>
      </div>

      <div className="read-progress-bar">
        <div className="read-progress-fill" style={{ width: `${readPct}%` }} />
      </div>

      <div className="content-scroll">
        <div className="content-inner">
          <h2 className="content-title">{moduleTitle}</h2>

          {notebook.cells.map((cell, i) => {
            const source = getCellSource(cell.source);
            if (!source.trim()) return null;

            if (cell.cell_type === 'markdown') {
              return (
                <div key={i} className="md-cell">
                  <ReactMarkdown remarkPlugins={[remarkGfm]}>{source}</ReactMarkdown>
                </div>
              );
            }

            if (cell.cell_type === 'code') {
              const outputText = cell.outputs
                ?.filter(o => o.output_type === 'stream' && o.text)
                .flatMap(o => o.text ?? []) ?? [];
              return <CodeBlock key={i} code={source} output={outputText} />;
            }

            return null;
          })}

          <div className="reader-footer">
            <div className="nav-buttons">
              <button className="nav-btn prev-btn" onClick={onPrev} disabled={!hasPrev}>
                ← Anterior
              </button>
              <div className="nav-center-btns">
                {isCompleted && (
                  <button className="nav-btn redo-btn" onClick={onRedo} title="Desmarcar como concluído e refazer">
                    ↺ Refazer
                  </button>
                )}
                {!isCompleted && readPct >= 20 && (
                  <button className="nav-btn complete-btn" onClick={onComplete}>
                    ✓ Marcar como concluído
                  </button>
                )}
                {isCompleted && (
                  <button className="nav-btn complete-btn done" disabled>
                    ✓ Concluído
                  </button>
                )}
              </div>
              <button className="nav-btn next-btn" onClick={onNext} disabled={!hasNext}>
                Próximo →
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default NotebookReader;
