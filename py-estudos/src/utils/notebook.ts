import type { Notebook } from '../types';

export async function fetchNotebook(filename: string): Promise<Notebook | null> {
    try {
        const res = await fetch(`/${filename}`);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return await res.json();
    } catch (e) {
        console.error('Failed to load notebook:', filename, e);
        return null;
    }
}

export function getCellSource(source: string[]): string {
    return source.join('');
}
