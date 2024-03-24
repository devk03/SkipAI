"use client";

import React, { useState } from "react";
import { extactKey, postLecture } from "./utility";
import { useCookies } from "react-cookie";

function QueryPage() {
  const [cookies] = useCookies(["PHPSESSID"]); // Only interested in reading cookies
  console.log(cookies);
  const [inputText, setInputText] = useState("");
  async function postLecture(lectureKey: string) {
    const url = `http://127.0.0.1:5000/fetchLecture?lectureKey=${lectureKey}`;
    const response = await fetch(url);
    return response;
  }
  const handleButtonClick = () => {
    const key = extactKey(inputText ?? "");
    postLecture(key || "");
  };

  return (
    <>
      <input
        type="text"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
      />
      <button onClick={handleButtonClick}>Submit</button>
    </>
  );
}
export default QueryPage;
