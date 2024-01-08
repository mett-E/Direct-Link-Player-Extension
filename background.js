function sendCommandToPython(link) {
  const message = { command: link };
  chrome.runtime.sendNativeMessage('com.metti.pythonnativehost', message);
}

chrome.contextMenus.onClicked.addListener(function(info, tab) {
  if (info.menuItemId === "pythonNativeContextMenu") {
    const href = info.linkUrl;
    sendCommandToPython(href)
}});

chrome.contextMenus.create({
  title: "Open in Player",
  id: "pythonNativeContextMenu",
  contexts: ["all"],
});
