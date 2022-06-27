import { signOut } from 'firebase/auth';
import React from 'react'
import { useAuthState } from 'react-firebase-hooks/auth'
import PageLayout from '../components/common/Layout'
import { auth, db } from '../firebase/config'

function Profile() {
  const [user] = useAuthState(auth);
  return (
    <PageLayout>
        <div>{user?.displayName}</div>
        <button onClick={()=>signOut(auth)}>SignOut</button>
    </PageLayout>
  )
}

export default Profile