import React, { useState } from 'react'
import PageLayout from '../common/Layout';
import SignIn from './SignIn';
import SignUp from './SignUp';

function AuthScreen() {
    const [signInPage, setSignInPage] = useState(true)
    const change = () => {
        setSignInPage(!signInPage);
    }
    return (
        <PageLayout>
            <div className="h-full w-full grid place-items-center">
                <div className="h-1/2 bg-red-400 w-1/2 rounded-xl flex flex-col">
                    <h1 className="text-center text-3xl py-3 bg-yellow-500 rounded-t-xl font-bold">
                        Welcome to Coderecs
                    </h1>
                    {signInPage ? (
                        <SignIn change={change} />
                    ) : (
                        <SignUp change={change} />
                    )}
                </div>
            </div>
        </PageLayout>
    )
}

export default AuthScreen