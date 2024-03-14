// Firebase App
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyD400cVgIygpzM30Y8aE3OnQtWq_jmyEPg",
  authDomain: "skipai-fd355.firebaseapp.com",
  projectId: "skipai-fd355",
  storageBucket: "skipai-fd355.appspot.com",
  messagingSenderId: "477755436582",
  appId: "1:477755436582:web:9ebbfbc04e96b0661cc0e7",
  measurementId: "G-5PCYDMDF6Q",
};

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);

// Export the firebase app
export default firebaseApp;