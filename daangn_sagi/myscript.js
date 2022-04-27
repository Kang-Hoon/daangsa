var now = new Date(); // 시간 정보 객체 생성
var xtru = 1;
var xfal = 0;

document.write("Hello World!\n");
document.write("How are you doing?");

chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
}); 
