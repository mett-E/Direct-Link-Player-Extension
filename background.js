function sendCommandToPython(com) {
  // alert(com)
  const message = { command: com };
  chrome.runtime.sendNativeMessage('com.example.pythonnativehost', message);
  // alert("done")
}

chrome.contextMenus.onClicked.addListener(function(info, tab) {
  if (info.menuItemId === "pythonNativeContextMenu") {
    const href = info.linkUrl;
    sendCommandToPython(href)
}});

chrome.contextMenus.create({
  title: "Open with MPV",
  id: "pythonNativeContextMenu",
  contexts: ["all"],
});
