import '../styles/globals.css'
import type { AppProps } from 'next/app'

function MyApp({ Component, pageProps }: AppProps) {
  const App = Component;
  return <App {...pageProps} />
}

export default MyApp
