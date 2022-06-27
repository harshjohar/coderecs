import { useAuthState } from 'react-firebase-hooks/auth'
import LandingPage from '../components/LandingPage/LandingPage';
import { auth } from '../firebase/config'
import '../styles/globals.css'

function MyApp({ Component, pageProps }) {
    const [user, loading] = useAuthState(auth);

    if(!user) {
        return <LandingPage />
    }
    return <Component {...pageProps} />
}

export default MyApp
