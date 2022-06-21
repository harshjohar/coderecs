import Link from 'next/link'
import { signInWithPopup, signOut } from 'firebase/auth'
import { auth, provider } from '../../firebase/config'
import { useAuthState } from 'react-firebase-hooks/auth'

function Navbar() {
    const [user] = useAuthState(auth)
    return (
        <header className="flex justify-between bg-teal-900 px-20">
            <div className="flex items-center space-x-20">
                <Link href={'/'}>
                    <img
                        src="/assets/images/logo.png"
                        alt=""
                        className="w-36 cursor-pointer object-contain"
                    />
                </Link>
                <div className="hidden items-center space-x-10 md:inline-flex text-white">
                    <Link href={'/about'}>About</Link>
                    <Link href={'/contact'}>Contact</Link>
                    <Link
                        href={'/editor/ide'}
                        className="rounded-full bg-green-600 px-4 py-1 text-white"
                    >
                        IDE
                    </Link>
                </div>
            </div>
            <div className="flex items-center space-x-5 text-white">
                {!user ? (
                    <button
                        className="cursor-pointer rounded-full px-4 py-1 hover:bg-amber-500 hover:text-black"
                        onClick={() => signInWithPopup(auth, provider)}
                    >
                        Sign In
                    </button>
                ) : (
                    <button
                        className="cursor-pointer rounded-full px-4 py-1"
                        onClick={() => signOut(auth)}
                    >
                        Hi! {user.displayName}
                    </button>
                )}
                <Link href={'idea'}>
                <h3 className="cursor-pointer rounded-full px-4 py-1 hover:bg-amber-500 hover:text-black">
                    How this works?
                </h3>
                </Link>
            </div>
        </header>
    )
}

export default Navbar
