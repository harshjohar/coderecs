import Link from 'next/link'
import React from 'react'


function Navbar() {
    return (
        <header className="flex justify-between bg-coderecs-bgNav px-20 tshadow p-2">
            <div className="flex items-center space-x-20">
                <p className="text-coderecs-textLight text-[2.4rem]">Coderecs</p>
                <div className="hidden items-center space-x-10 md:inline-flex text-coderecs-textLight">
                    <Link href={'/about'}><p>About</p></Link>
                    <Link href={'/contact'}><p>Contact</p></Link>
                    <Link href={'idea'}>
                        <button className="cursor-pointer rounded-full px-4 py-1 hover:opacity-90">
                           How This Works
                        </button>
                </Link>
                </div>
            </div>
            <div className="flex items-center space-x-5 text-coderecs-textLight">
                
                    <Link href={'/profile'}>
                        <button className="cursor-pointer rounded-full px-4 py-1 hover:opacity-90">
                           User
                        </button>
                    </Link>
            </div>
        </header>
  )
}

export default Navbar