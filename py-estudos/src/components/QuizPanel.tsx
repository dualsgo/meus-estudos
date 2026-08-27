import React, { useState } from 'react';
import type { Quiz } from '../types';
import './QuizPanel.css';

interface QuizPanelProps {
  moduleId: string;
  quizzes: Quiz[];
  onScore: (score: number) => void;
  savedScore?: number;
}

const QuizPanel: React.FC<QuizPanelProps> = ({ quizzes, onScore, savedScore }) => {
  const [current, setCurrent] = useState(0);
  const [selected, setSelected] = useState<number | null>(null);
  const [submitted, setSubmitted] = useState(false);
  const [answers, setAnswers] = useState<boolean[]>([]);
  const [showScore, setShowScore] = useState(!!savedScore);
  const [, setFinished] = useState(!!savedScore);

  const q = quizzes[current];
  const isCorrect = submitted && selected === q?.correctIndex;

  const handleSubmit = () => {
    if (selected === null) return;
    setSubmitted(true);
    setAnswers(prev => [...prev, selected === q.correctIndex]);
  };

  const handleNext = () => {
    if (current < quizzes.length - 1) {
      setCurrent(c => c + 1);
      setSelected(null);
      setSubmitted(false);
    } else {
      // answers já inclui a última resposta (adicionada por handleSubmit).
      // Não adicionar selected novamente para evitar dupla contagem.
      const score = Math.round((answers.filter(Boolean).length / quizzes.length) * 100);
      setShowScore(true);
      onScore(score);
    }
  };

  const handleRetry = () => {
    setCurrent(0);
    setSelected(null);
    setSubmitted(false);
    setAnswers([]);
    setFinished(false);
    setShowScore(false);
  };

  if (quizzes.length === 0) {
    return (
      <div className="quiz-empty">
        <span>🚧</span>
        <p>Quiz em breve!</p>
        <small>Exercícios serão adicionados para este módulo.</small>
      </div>
    );
  }

  if (showScore) {
    const sc = savedScore ?? Math.round((answers.filter(Boolean).length / quizzes.length) * 100);
    const grade = sc >= 80 ? 'excellent' : sc >= 60 ? 'good' : 'try-again';
    const emoji = sc >= 80 ? '🏆' : sc >= 60 ? '👍' : '💪';
    const msg = sc >= 80 ? 'Excelente! Dominado!' : sc >= 60 ? 'Bom trabalho!' : 'Continue praticando!';
    return (
      <div className="quiz-score">
        <div className={`score-circle ${grade}`}>
          <span className="score-emoji">{emoji}</span>
          <span className="score-num">{sc}%</span>
        </div>
        <p className="score-msg">{msg}</p>
        <p className="score-detail">{answers.filter(Boolean).length}/{quizzes.length} corretas</p>
        <button className="quiz-retry-btn" onClick={handleRetry}>Tentar novamente</button>
      </div>
    );
  }

  return (
    <div className="quiz-panel">
      <div className="quiz-header">
        <span className="quiz-icon">📝</span>
        <span className="quiz-title">Exercício</span>
        <span className="quiz-progress">{current + 1}/{quizzes.length}</span>
      </div>

      <div className="quiz-progress-dots">
        {quizzes.map((_, i) => (
          <div
            key={i}
            className={`quiz-dot ${i < current ? 'done' : i === current ? 'active' : ''}`}
          />
        ))}
      </div>

      <p className="quiz-question">{q.question}</p>

      <div className="quiz-options">
        {q.options.map((opt, i) => {
          let cls = 'quiz-option';
          if (submitted) {
            if (i === q.correctIndex) cls += ' correct';
            else if (i === selected) cls += ' wrong';
            else cls += ' dimmed';
          } else if (selected === i) {
            cls += ' selected';
          }
          return (
            <button
              key={i}
              className={cls}
              onClick={() => !submitted && setSelected(i)}
              disabled={submitted}
            >
              <span className="opt-letter">{String.fromCharCode(65 + i)}</span>
              <span className="opt-text">{opt}</span>
              {submitted && i === q.correctIndex && <span className="opt-check">✓</span>}
              {submitted && i === selected && i !== q.correctIndex && <span className="opt-x">✗</span>}
            </button>
          );
        })}
      </div>

      {submitted && (
        <div className={`quiz-feedback ${isCorrect ? 'feedback-correct' : 'feedback-wrong'}`}>
          <p className="feedback-title">{isCorrect ? '✓ Correto!' : '✗ Incorreto'}</p>
          <p className="feedback-exp">{q.explanation}</p>
        </div>
      )}

      <div className="quiz-actions">
        {!submitted ? (
          <button
            className="quiz-btn submit-btn"
            onClick={handleSubmit}
            disabled={selected === null}
          >
            Verificar Resposta
          </button>
        ) : (
          <button className="quiz-btn next-q-btn" onClick={handleNext}>
            {current < quizzes.length - 1 ? 'Próxima questão →' : 'Ver resultado →'}
          </button>
        )}
      </div>
    </div>
  );
};

export default QuizPanel;
