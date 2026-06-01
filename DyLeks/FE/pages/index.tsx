import { useRouter } from 'next/router';
import Head from 'next/head';
import styles from '../styles/Home.module.css';
import { useTheme } from '../contexts/ThemeContext';
import BatMascot from '../components/BatMascot';
import ButterflyMascot from '../components/ButterflyMascot';
import ThemeToggle from '../components/ThemeToggle';

export default function Home() {
  const router = useRouter();
  const { theme } = useTheme();

  const handleStart = () => {
    router.push('/screening');
  };

  return (
    <>
      <div className="background-container">
        <div className="star" style={{ top: '20%', left: '30%', animationDelay: '0s' }}></div>
        <div className="star" style={{ top: '70%', left: '80%', animationDelay: '1s' }}></div>
        <div className="star" style={{ top: '40%', left: '60%', animationDelay: '2s' }}></div>
      </div>

      <div className={styles.container}>
        <Head>
          <title>DyLeks - Deteksi Dini & Belajar Adaptif</title>
          <meta name="description" content="Platform skrining dini dan belajar adaptif multisensori ramah anak disleksia." />
        </Head>

        <ThemeToggle />

        <div className={styles.centered}>
          <div className={styles.mascotContainer}>
            {theme === 'dark' ? <BatMascot /> : <ButterflyMascot />}
          </div>
          <h1 className={styles.title}>DyLeks <span className={styles.highlight}>{theme === 'dark' ? 'Night' : 'Day'}</span></h1>
          <p className={styles.subtitle}>
            {theme === 'dark' 
              ? 'Membaca menjadi petualangan menembus malam.'
              : 'Terbang bersama kupu-kupu belajar membaca!'}
          </p>
        </div>

        <button className={styles.button} onClick={handleStart}>
          <span className={styles.btnText}>Mulai Petualangan</span>
          <svg className={styles.iconRight} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </button>
      </div>
    </>
  );
}
