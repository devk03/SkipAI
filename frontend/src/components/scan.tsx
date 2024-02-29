import React from "react";
import { useState } from "react";
function Scan() {
  const [trackElement, setTrackElement] = useState();
  const [transcript, setTranscript] = useState("");
  const [question, setQuestion] = useState("");
  const handleChange = (event: any) => {
    setQuestion(event.target.value);
  };
  const handleSubmission = () => {
    console.log("Submitted:", question);
  };
  const handleButtonClick = () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs.length > 0 && tabs[0].id !== undefined) {
        chrome.tabs.sendMessage(
          tabs[0].id,
          { action: "queryTrackElement" },
          (response) => {
            if (response) {
              // Update state with the track element's outerHTML
              setTrackElement(response);
              // Regular expression to find the 'rk' parameter and capture its value
              console.log("Track element found:", trackElement);
              const srcRegex = /src="([^"]+)"/;

              // Extracting the src attribute
              const match = response.trackElement.match(srcRegex);
              const src = match ? match[1] : null;

              // Assuming src contains the URL, use a regular expression to extract the rk parameter
              const rkRegex = /rk=([^&]+)/;
              const rkMatch = src ? src.match(rkRegex) : null;
              const rkValue = rkMatch ? rkMatch[1] : null;
              console.log(rkValue); // Outputs: bN2TOQ
              const url = `https://leccap.engin.umich.edu/leccap/player/api/webvtt/?rk=${rkValue}`;

              fetch(url)
                .then((response) => {
                  if (!response.ok) {
                    throw new Error("Network response was not ok");
                  }
                  return response.text(); // or response.json() if the response is JSON
                })
                .then((data) => {
                  console.log(data); // Process your data here
                  setTranscript(data);
                })
                .catch((error) => {
                  console.error(
                    "There was a problem with your fetch operation:",
                    error
                  );
                });
            } else {
              // Handle case where no track element is found
              console.log("Track element not found");
            }
          }
        );
      } else {
        console.log("No active tab found");
      }
    });
  };

  return (
    <>
      {!transcript ? (
        <button onClick={handleButtonClick}>SkipAI</button>
      ) : (
        <>
          <input type="text" value={question} onChange={handleChange} />
          <button onClick={handleSubmission}>Submit</button>
        </>
      )}
    </>
  );
}

export default Scan;
