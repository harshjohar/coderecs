import { signInWithEmailAndPassword } from 'firebase/auth'
import React, { useEffect, useState } from 'react'
import { auth } from '../../firebase/config'
import { useRouter } from 'next/router'

function SignIn({ change }) {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [errorMessage, setErrorMessage] = useState('')
    const router = useRouter()
    const signIn = () => {
        signInWithEmailAndPassword(auth, email, password)
            .then((res) => {
                router.push('/')
            })
            .catch((e) => setErrorMessage(e.message))
    }

    return (
        <>
            <div className="flex flex-col my-10 px-10">
                <input
                    type="text"
                    className="outline-none py-2 px-4 m-3 rounded-full text-center"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input
                    type="password"
                    className="outline-none py-2 px-4 m-3 rounded-full text-center"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
            </div>
            {errorMessage && (
                    <p className='text-center italic text-red-900'>{errorMessage}</p>
            )}
            <button
                onClick={signIn}
                className="mx-auto text-black font-bold cursor-pointer outline-none py-2 px-4 m-3 rounded-full text-center bg-yellow-500"
            >
                Sign In
            </button>
            <p className="text-center">
                Don't have an account?{' '}
                <span
                    className="text-yellow-500 font-bold underline cursor-pointer hover:text-yellow-400"
                    onClick={change}
                >
                    Sign Up Now!
                </span>
            </p>
        </>
    )
}

export default SignIn
