import React from 'react';
import { useTheme } from '../contexts/ThemeContext';

const ThemeToggle: React.FC = () => {
  const { theme, toggleTheme } = useTheme();

  return (
    <button 
      onClick={toggleTheme}
      style={{
        position: 'absolute',
        top: '20px',
        right: '20px',
        background: 'var(--glass-bg)',
        border: '1px solid var(--glass-border)',
        color: 'var(--text-main)',
        padding: '10px 15px',
        borderRadius: '20px',
        cursor: 'pointer',
        boxShadow: 'var(--glass-shadow)',
        display: 'flex',
        alignItems: 'center',
        gap: '8px',
        zIndex: 100,
        fontWeight: 'bold'
      }}
    >
      {theme === 'dark' ? '🦇 Bat Mode' : '🦋 Butterfly Mode'}
    </button>
  );
};

export default ThemeToggle;
