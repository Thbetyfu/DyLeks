import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import styles from '../styles/Summary.module.css';
import Head from 'next/head';
import ThemeToggle from '../components/ThemeToggle';
import { useTheme } from '../contexts/ThemeContext';
import BatMascot from '../components/BatMascot';
import ButterflyMascot from '../components/ButterflyMascot';

export default function Summary() {
  const router = useRouter();
  const { theme } = useTheme();
  const [mounted, setMounted] = useState(false);
  const [correctCount, setCorrectCount] = useState(0);
  const [totalCount, setTotalCount] = useState(0);

  useEffect(() => {
    setMounted(true);
    
    const exerciseData = sessionStorage.getItem('exercise_analytics');
    const screeningData = sessionStorage.getItem('dyslexia_screening_results');

    if (exerciseData) {
      const parsed = JSON.parse(exerciseData);
      setTotalCount(parsed.length);
      setCorrectCount(parsed.filter((p: any) => p.isCorrect).length);
    } else if (screeningData) {
      const parsed = JSON.parse(screeningData);
      setTotalCount(parsed.length);
      setCorrectCount(parsed.filter((p: any) => p.result.risk_score <= 40).length);
    }
  }, []);

  if (!mounted) return null;

  return (
    <>
      <div className="background-container">
        <div className="star" style={{ top: '15%', left: '25%', animationDelay: '0s' }}></div>
        <div className="star" style={{ top: '65%', left: '75%', animationDelay: '1s' }}></div>
        <div className="star" style={{ top: '35%', left: '55%', animationDelay: '2s' }}></div>
      </div>

      <div className={styles.container}>
        <Head>
          <title>Selesai Screening - DyLeks</title>
        </Head>

        <ThemeToggle />

        <h1 className={styles.headline}>
          Kamu hebat sekali!
        </h1>
        <p className={styles.subheadline}>
          Tepat {correctCount} dari {totalCount} kata
        </p>

        <div className={styles.mascotContainer}>
          {theme === 'dark' ? <BatMascot className={styles.duck} /> : <ButterflyMascot className={styles.duck} />}
        </div>

        <p className={styles.subheadline}>
          Kita lihat hasil latihan yang cocok untukmu ya!
        </p>

        <div className={styles.footer}>
          <button className={styles.button} onClick={() => router.push('/result')}>
            Lihat Hasil
          </button>
        </div>
      </div>
    </>
  );
}
