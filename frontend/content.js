/// <reference types="chrome"/>
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "queryTrackElement") {
    const trackElement = document.querySelector("track");
    console.log(trackElement);
    sendResponse({
      trackElement: trackElement ? trackElement.outerHTML : null,
    });
  }
});
