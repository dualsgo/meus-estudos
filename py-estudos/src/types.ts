export interface NotebookCell {
  cell_type: 'markdown' | 'code';
  source: string[];
  outputs?: Array<{
    output_type: string;
    text?: string[];
    name?: string;
  }>;
  execution_count?: number | null;
}

export interface Notebook {
  cells: NotebookCell[];
  metadata?: Record<string, unknown>;
}

export interface Module {
  id: string;
  number: number;
  title: string;
  filename: string;
  status: 'completed' | 'current' | 'locked';
  quizScore?: number;
}

export interface Quiz {
  question: string;
  options: string[];
  correctIndex: number;
  explanation: string;
}

export interface Progress {
  completedModules: string[];
  quizScores: Record<string, number>;
  streak: number;
  lastVisited: string;
  weeklyProgress: number[];
}
