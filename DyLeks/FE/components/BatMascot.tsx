import React from 'react';

const BatMascot: React.FC<{ className?: string }> = ({ className }) => {
  return (
    <svg className={className} viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="batGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="var(--highlight)" />
          <stop offset="100%" stopColor="var(--accent)" />
        </linearGradient>
        <filter id="batGlow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="5" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <style>{`
          .bat-wing {
            transform-origin: center;
            animation: batFlap 0.5s infinite alternate ease-in-out;
          }
          @keyframes batFlap {
            0% { transform: scaleY(1); }
            100% { transform: scaleY(0.85); }
          }
        `}</style>
      </defs>
      {/* Bat Wings */}
      <path className="bat-wing" d="M100 80 Q 50 20 10 50 Q 30 80 15 110 Q 50 100 70 140 Q 80 110 100 110 Z" fill="url(#batGrad)" />
      <path className="bat-wing" d="M100 80 Q 150 20 190 50 Q 170 80 185 110 Q 150 100 130 140 Q 120 110 100 110 Z" fill="url(#batGrad)" />
      {/* Bat Body */}
      <circle cx="100" cy="95" r="25" fill="var(--primary)" stroke="url(#batGrad)" strokeWidth="4" filter="url(#batGlow)"/>
      {/* Bat Ears */}
      <polygon points="85,75 75,45 95,72" fill="var(--highlight)" />
      <polygon points="115,75 125,45 105,72" fill="var(--highlight)" />
      {/* Bat Eyes */}
      <ellipse cx="90" cy="95" rx="5" ry="8" fill="var(--highlight)" />
      <ellipse cx="110" cy="95" rx="5" ry="8" fill="var(--highlight)" />
      {/* Eye shine */}
      <circle cx="89" cy="92" r="2" fill="#FFF" />
      <circle cx="109" cy="92" r="2" fill="#FFF" />
    </svg>
  );
};

export default BatMascot;
