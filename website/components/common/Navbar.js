import Link from 'next/link'
import { signInWithPopup, signOut } from 'firebase/auth'
import { auth, provider } from '../../firebase/config'
import { useAuthState } from 'react-firebase-hooks/auth'
import Image from 'next/image';

function Navbar() {
    const [user] = useAuthState(auth)
    return (
        <header className="flex justify-between bg-green-800 px-20">
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
                <Link href={'idea'}>
                    <h3 className="hidden lg:inline-flex cursor-pointer rounded-full px-4 py-1 hover:bg-amber-500 hover:text-black">
                        How this works?
                    </h3>
                </Link>
                {!user ? (
                    <button
                        className="cursor-pointer rounded-full px-4 py-1 hover:bg-amber-500 hover:text-black"
                        onClick={() => signInWithPopup(auth, provider)}
                    >
                        Sign In
                    </button>
                ) : (
                    <Link href={'/profile'}>
                        <button className="cursor-pointer rounded-full px-4 py-1">
                            <Image src={user.photoURL} height={50} width={50} objectFit={'contain'} className="rounded-full" />
                        </button>
                    </Link>
                )}
            </div>
        </header>
    )
}

export default Navbar
