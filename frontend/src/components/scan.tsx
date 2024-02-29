import React from "react";
import { useState } from "react";
function Scan() {
  const [trackElement, setTrackElement] = useState();
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

  return <button onClick={handleButtonClick}>Query Track Element</button>;
}

export default Scan;
