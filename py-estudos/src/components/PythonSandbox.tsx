import React, { useEffect, useRef, useState, useCallback } from 'react';
import type { Notebook } from '../types';
import { getCellSource } from '../utils/notebook';
import './PythonSandbox.css';

declare global {
  interface Window {
    loadPyodide: (opts: { indexURL: string }) => Promise<PyodideInstance>;
    pyodideInstance?: PyodideInstance;
  }
}

interface PyodideInstance {
  runPythonAsync: (code: string) => Promise<unknown>;
  setStdout: (opts: { batched: (s: string) => void }) => void;
  setStderr: (opts: { batched: (s: string) => void }) => void;
}

interface PythonSandboxProps {
  notebook: Notebook | null;
  moduleTitle: string;
}

const PYODIDE_VERSION = '0.27.3';
const PYODIDE_CDN = `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/pyodide.js`;

const STARTER_CODE = `# Digite seu código Python aqui e clique em ▶ Executar
print("Olá, Python! 🐍")

# Experimente qualquer coisa:
nome = "Estudante"
print(f"Bem-vindo, {nome}!")
`;

type SandboxStatus = 'idle' | 'loading-pyodide' | 'ready' | 'running' | 'error-load';

interface OutputLine {
  text: string;
  type: 'stdout' | 'stderr' | 'info';
}

const PythonSandbox: React.FC<PythonSandboxProps> = ({ notebook, moduleTitle }) => {
  const [status, setStatus] = useState<SandboxStatus>('idle');
  const [code, setCode] = useState(STARTER_CODE);
  const [output, setOutput] = useState<OutputLine[]>([]);
  const [executionTime, setExecutionTime] = useState<number | null>(null);
  const pyodideRef = useRef<PyodideInstance | null>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const outputRef = useRef<HTMLDivElement>(null);

  // Load Pyodide on demand
  const loadPyodide = useCallback(async () => {
    if (pyodideRef.current) return true;
    if (window.pyodideInstance) {
      pyodideRef.current = window.pyodideInstance;
      return true;
    }
    setStatus('loading-pyodide');
    try {
      // Inject script if not already loaded
      if (!document.querySelector(`script[src="${PYODIDE_CDN}"]`)) {
        await new Promise<void>((resolve, reject) => {
          const s = document.createElement('script');
          s.src = PYODIDE_CDN;
          s.onload = () => resolve();
          s.onerror = () => reject(new Error('Falha ao carregar Pyodide'));
          document.head.appendChild(s);
        });
      }
      const pyodide = await window.loadPyodide({
        indexURL: `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`,
      });
      window.pyodideInstance = pyodide;
      pyodideRef.current = pyodide;
      setStatus('ready');
      return true;
    } catch {
      setStatus('error-load');
      return false;
    }
  }, []);

  const runCode = useCallback(async () => {
    const py = pyodideRef.current;
    if (!py || !code.trim()) return;

    setStatus('running');
    setOutput([]);
    setExecutionTime(null);
    const lines: OutputLine[] = [];
    const start = performance.now();

    py.setStdout({ batched: (s) => lines.push({ text: s, type: 'stdout' }) });
    py.setStderr({ batched: (s) => lines.push({ text: s, type: 'stderr' }) });

    try {
      await py.runPythonAsync(code);
    } catch (err: unknown) {
      const msg = err instanceof Error ? err.message : String(err);
      lines.push({ text: msg, type: 'stderr' });
    }

    const elapsed = performance.now() - start;
    setExecutionTime(Math.round(elapsed));
    setOutput(lines);
    setStatus('ready');

    setTimeout(() => outputRef.current?.scrollIntoView({ behavior: 'smooth', block: 'nearest' }), 50);
  }, [code]);

  // Handle Tab key in textarea
  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      const ta = textareaRef.current!;
      const start = ta.selectionStart;
      const end = ta.selectionEnd;
      const newVal = code.substring(0, start) + '    ' + code.substring(end);
      setCode(newVal);
      setTimeout(() => { ta.selectionStart = ta.selectionEnd = start + 4; }, 0);
    }
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      e.preventDefault();
      if (status === 'ready') runCode();
    }
  };

  // Extract first example code cell from notebook as starter
  const loadExampleFromModule = () => {
    if (!notebook) return;
    const firstCode = notebook.cells.find(c => c.cell_type === 'code' && getCellSource(c.source).trim());
    if (firstCode) {
      setCode(getCellSource(firstCode.source));
      setOutput([]);
    }
  };

  // Auto-scroll output
  useEffect(() => {
    if (output.length > 0 && outputRef.current) {
      outputRef.current.scrollTop = outputRef.current.scrollHeight;
    }
  }, [output]);

  const isLoaded = status === 'ready' || status === 'running';

  return (
    <div className="sandbox">
      <div className="sandbox-toolbar">
        <div className="sandbox-info">
          <span className="sandbox-icon">⚡</span>
          <span className="sandbox-title">Python Sandbox</span>
          <span className={`sandbox-status-dot ${status}`} title={
            status === 'idle' ? 'Clique em Inicializar'
            : status === 'loading-pyodide' ? 'Carregando Pyodide...'
            : status === 'ready' ? 'Pronto'
            : status === 'running' ? 'Executando...'
            : 'Erro ao carregar'
          } />
        </div>
        <div className="sandbox-actions">
          {notebook && isLoaded && (
            <button
              className="sandbox-btn example-btn"
              onClick={loadExampleFromModule}
              title={`Carregar exemplo de "${moduleTitle}"`}
            >
              📖 Exemplo do módulo
            </button>
          )}
          <button
            className="sandbox-btn clear-btn"
            onClick={() => { setCode(STARTER_CODE); setOutput([]); setExecutionTime(null); }}
            disabled={!isLoaded}
          >
            🗑 Limpar
          </button>
          {!isLoaded ? (
            <button
              className="sandbox-btn init-btn"
              onClick={loadPyodide}
              disabled={status === 'loading-pyodide' || status === 'error-load'}
            >
              {status === 'loading-pyodide' ? (
                <><span className="spin">⟳</span> Carregando...</>
              ) : status === 'error-load' ? (
                '⚠ Erro — Tentar novamente'
              ) : (
                '🚀 Inicializar Python'
              )}
            </button>
          ) : (
            <button
              className="sandbox-btn run-btn"
              onClick={runCode}
              disabled={status === 'running'}
            >
              {status === 'running' ? <><span className="spin">⟳</span> Executando...</> : '▶ Executar'}
            </button>
          )}
        </div>
      </div>

      {!isLoaded && status !== 'loading-pyodide' && status !== 'error-load' && (
        <div className="sandbox-idle-msg">
          <p>🐍 Clique em <strong>Inicializar Python</strong> para carregar o interpretador.</p>
          <small>Pyodide v{PYODIDE_VERSION} — Python real rodando no seu navegador via WebAssembly.<br/>Download único de ~10MB. Sem servidor externo.</small>
        </div>
      )}

      {status === 'loading-pyodide' && (
        <div className="sandbox-loading">
          <div className="loading-snake">🐍</div>
          <p>Carregando interpretador Python...</p>
          <small>Primeira vez pode levar alguns segundos</small>
        </div>
      )}

      {status === 'error-load' && (
        <div className="sandbox-error-msg">
          <span>⚠️</span>
          <p>Falha ao carregar Pyodide. Verifique sua conexão com a internet.</p>
          <button className="sandbox-btn init-btn" onClick={loadPyodide}>Tentar novamente</button>
        </div>
      )}

      <div className={`sandbox-editor-wrap ${!isLoaded ? 'hidden' : ''}`}>
        <div className="editor-header">
          <div className="code-dots">
            <span className="dot red" /><span className="dot yellow" /><span className="dot green" />
          </div>
          <span className="editor-filename">script.py</span>
          <span className="editor-hint">Ctrl+Enter para executar • Tab para indentar</span>
        </div>
        <textarea
          ref={textareaRef}
          className="sandbox-textarea"
          value={code}
          onChange={e => setCode(e.target.value)}
          onKeyDown={handleKeyDown}
          spellCheck={false}
          autoComplete="off"
          autoCorrect="off"
          autoCapitalize="off"
          placeholder="# Digite seu código Python aqui..."
          rows={12}
        />
      </div>

      {isLoaded && (
        <div className="sandbox-output-wrap">
          <div className="output-header">
            <span className="output-label-text">▶ Saída</span>
            {executionTime !== null && (
              <span className="exec-time">⏱ {executionTime}ms</span>
            )}
          </div>
          <div className="sandbox-output" ref={outputRef}>
            {output.length === 0 && status === 'ready' && (
              <span className="output-placeholder">A saída do seu código aparecerá aqui...</span>
            )}
            {status === 'running' && output.length === 0 && (
              <span className="output-running">⟳ Executando...</span>
            )}
            {output.map((line, i) => (
              <div key={i} className={`output-line ${line.type}`}>
                {line.text}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default PythonSandbox;
