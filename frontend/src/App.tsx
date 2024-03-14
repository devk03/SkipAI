import Scan from "./components/scan";
import firebaseApp from "./firebaseConfig";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
function App() {
  const handleSignIn = () => {
    const auth = getAuth(firebaseApp); // Pass the initialized app to getAuth
    const provider = new GoogleAuthProvider();
    signInWithPopup(auth, provider)
      .then((result) => {
        const credential = GoogleAuthProvider.credentialFromResult(result);
        const token = credential?.accessToken;
        const user = result.user;
        // Use the token and user information as needed
        console.log(token, user);
      })
      .catch((error: any) => {
        // Handle Errors here
        console.error(error);
      });
  };
  return (
    <>
      <h1>Skip AI</h1>
      <h4>
        SkipAI is a tool to help you skip the bullshit and help you find what is
        important.
      </h4>
      <button onClick={handleSignIn}>Click me</button>
      <Scan />
    </>
  );
}

export default App;
