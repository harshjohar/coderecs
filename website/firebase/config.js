import { initializeApp } from "firebase/app";
import {getFirestore} from 'firebase/firestore';
import {getAuth, GoogleAuthProvider} from 'firebase/auth';

const firebaseConfig = {
  apiKey: "AIzaSyD0sU3nzBBPXKFNXMmXzOn4NVFGU7ZVIbU",
  authDomain: "coding-platform-3f3d7.firebaseapp.com",
  projectId: "coding-platform-3f3d7",
  storageBucket: "coding-platform-3f3d7.appspot.com",
  messagingSenderId: "248797448968",
  appId: "1:248797448968:web:3e0699e316dda2f403fabd"
};

initializeApp(firebaseConfig);
const db = getFirestore();
const auth = getAuth()
const provider = new GoogleAuthProvider();

export {db, auth, provider};