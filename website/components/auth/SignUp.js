import {
    createUserWithEmailAndPassword,
    sendEmailVerification,
    updateProfile,
} from 'firebase/auth'
import React, { useState } from 'react'
import { auth } from '../../firebase/config'

function SignUp({ change }) {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [displayName, setDisplayName] = useState('')
    const [errorMessage, setErrorMessage] = useState('')

    const signUp = async () => {
        try {
            await createUserWithEmailAndPassword(auth, email, password).catch(
                (err) => setErrorMessage(err.message)
            )
            await sendEmailVerification(auth.currentUser).catch((err) =>
                setErrorMessage(err.message)
            )
            await updateProfile(auth.currentUser, {
                displayName: displayName,
            }).catch((err) => setErrorMessage(err.message))
        } catch (err) {
            setErrorMessage(err.message)
        }
    }
    return (
        <>
            <div className="flex flex-col px-10">
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
                <input
                    type="text"
                    className="outline-none py-2 px-4 m-3 rounded-full text-center"
                    placeholder="Codeforces handle"
                    value={displayName}
                    onChange={(e) => setDisplayName(e.target.value)}
                />
            </div>
            {errorMessage && (
                    <p className='text-center italic text-red-900'>{errorMessage}</p>
            )}
            <button
                onClick={signUp}
                className="mx-auto text-black font-bold cursor-pointer outline-none py-2 px-4 m-3 rounded-full text-center bg-yellow-500"
            >
                Sign Up
            </button>
            <p className="text-center">
                Already have an account?{' '}
                <span
                    className="text-yellow-500 font-bold underline cursor-pointer hover:text-yellow-400"
                    onClick={change}
                >
                    Sign In Now!
                </span>
            </p>
        </>
    )
}

export default SignUp
