const actionForm = document.querySelector("#actionForm");

// 목록으로 클릭 시 acthonForm 보내기
document.querySelector(".btn-success").addEventListener("click", (e) => {
  //e.preventDefault();
  actionForm.submit();
});

const elements = document.querySelectorAll(".delete");

elements.forEach((element) => {
  element.addEventListener("click", (e) => {
    if (confirm("정말로 삭제하시겠습니까?")) {
      location.href = e.target.dataset.url;
    }
  });
});
