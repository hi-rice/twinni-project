// static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript is working!");

    // 1. 사용자 리스트 클릭 이벤트 처리
    const userItems = document.querySelectorAll('li');
    userItems.forEach(function(item) {
        item.addEventListener('click', function() {
            alert(`You clicked on ${item.textContent}`);
        });
    });

    // 2. AJAX 요청을 통해 사용자 목록 로드
    function loadUsers() {
        fetch('/api/users/')
            .then(response => response.json())
            .then(data => {
                const userList = document.querySelector('ul');
                userList.innerHTML = '';  // 기존 리스트를 비우기
                data.forEach(user => {
                    const li = document.createElement('li');
                    li.textContent = `${user.username} - ${user.email}`;
                    userList.appendChild(li);
                });
            })
            .catch(error => console.error('Error fetching users:', error));
    }

    // 페이지 로드 시 사용자 목록을 가져옴
    loadUsers();

    // 3. 폼 제출 이벤트 처리
    const userForm = document.querySelector('form');
    if (userForm) {
        userForm.addEventListener('submit', function(event) {
            event.preventDefault();  // 기본 폼 제출 동작 방지
            const formData = new FormData(userForm);
            fetch('/api/users/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log('User created:', data);
                loadUsers();  // 새로운 사용자 목록 로드
            })
            .catch(error => console.error('Error creating user:', error));
        });
    }

    // 4. 로컬 저장소를 사용한 테마 관리
    const themeToggle = document.querySelector('#theme-toggle');
    const body = document.body;

    // 이전에 저장된 테마 로드
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        body.className = savedTheme;
    }

    // 테마 변경
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            if (body.className === 'dark-theme') {
                body.className = 'light-theme';
                localStorage.setItem('theme', 'light-theme');
            } else {
                body.className = 'dark-theme';
                localStorage.setItem('theme', 'dark-theme');
            }
        });
    }

    // 5. 버튼 클릭 시 애니메이션 효과 추가
    const animateButton = document.querySelector('#animate-button');
    const box = document.querySelector('.box');

    if (animateButton && box) {
        animateButton.addEventListener('click', function() {
            box.classList.add('move');
            setTimeout(function() {
                box.classList.remove('move');
            }, 1000);  // 애니메이션이 끝난 후 클래스를 제거
        });
    }
});