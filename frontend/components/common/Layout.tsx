import Head from 'next/head'
import React, { ReactNode } from 'react'
import Navbar from './Navbar'

function Layout({children} : {children : ReactNode}) {
  return (
    <div className="h-screen w-screen flex flex-col scrollbar-hide font-poppins">
            <Head>
                <title>Coderecs</title>
                <meta
                    name="description"
                    content="The coding platform, you always wanted!"
                />
                <link rel="icon" href="/assets/logo/favicon.ico" />
                <link rel="manifest" href="/assets/logo/manifest.json" />
                <link rel="apple-touch-icon" href="/assets/logo/apple-touch-icon.png" />
            </Head>
            <Navbar />
            <div className="flex-1 p-5">{children}</div>
        </div>
  )
}

export default Layout