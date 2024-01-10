Routes: 

---

- GET /: 

returns {ok: true}



- POST /removebg: 

needs body:
{
imageURL: string
}

returns {'image_data': base64_string}
