import Image from 'next/image'
import Link from 'next/link'
import { useState } from 'react'

function Navbar() {
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
                    <Link href={'/editor/ide'} className="rounded-full bg-green-600 px-4 py-1 text-white">
                        IDE
                    </Link>
                </div>
            </div>
            <div className="flex items-center space-x-5 text-white">
                <h3 className="cursor-pointer rounded-full px-4 py-1 hover:bg-amber-500 hover:text-black">Sign In</h3>
                <h3 className="cursor-pointer rounded-full px-4 py-1 hover:bg-amber-500 hover:text-black">
                    Get Started
                </h3>
            </div>
        </header>
    )
}

export default Navbar
