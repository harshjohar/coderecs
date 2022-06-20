import Navbar from '../components/common/Navbar'
import '../styles/globals.css'

function MyApp({ Component, pageProps }) {
  return (
    <>
    <Navbar/>
  <Component {...pageProps} />
    </>
  )
}

export default MyApp
