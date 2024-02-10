document.addEventListener('DOMContentLoaded', function (){
   const RegisterForm = document.getElementById('register-form')

    RegisterForm.addEventListener('submit', function (event){
        event.preventDefault();
        const formData = new FormData(RegisterForm)

        fetch(RegisterForm.action,{
           method: 'POST',
           body: formData ,
        })
        .then(response => {
            if (response.status === 200){
                window.location.href = '/users/login/'
            } else {
                console.log(response);
            }
        })
            .then(data => {
                Swal.fire({
                    icon: 'error',
                    title: 'Register Failed',
                    text: data.error,
                })
                    .then(() => {
                    window.location.href = '/users/register/';
                });
            })
    });
});