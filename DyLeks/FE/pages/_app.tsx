import type { AppProps } from 'next/app';
import { Poppins } from 'next/font/google';
import '../styles/globals.css';
import { ThemeProvider } from '../contexts/ThemeContext';

const poppins = Poppins({
  subsets: ['latin'],
  weight: ['400', '600', '700'],
  variable: '--font-poppins',
});

export default function App({ Component, pageProps }: AppProps) {
  return (
    <ThemeProvider>
      <main className={poppins.className}>
        <Component {...pageProps} />
      </main>
    </ThemeProvider>
  );
}
