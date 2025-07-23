# CodeLeap Test

During the previous assessment, most of the tasks involved concepts I had already studied and applied in personal projects. However, I encountered some complexity in implementing the "likes" functionality to add and remove interactions between users and posts. To overcome this challenge, I sought assistance from an AI, which helped me construct this specific part.

I'm committed to reviewing and improving this functionality, aiming to implement it more efficiently and in line with best practices.

### 🔹 Users (`/users/`)

| Method | Path       | Description        | Body JSON     |
|--------|------------|--------------------|----------------|
| GET    | `/users/`  | List all users      | —              |
| POST   | `/users/`  | Create a user       | `{ users }`    |

### 🔹 Specific User (`/users/:pk/`)

| Method | Path            | Description               | Body JSON     |
|--------|------------------|----------------------------|----------------|
| GET    | `/users/:pk/`   | Retrieve user details      | —              |
| PUT    | `/users/:pk/`   | Update user data           | `{ users }`    |
| DELETE | `/users/:pk/`   | Delete a user              | —              |

### 🔹 Posts (`/careers/`)

| Method | Path             | Description               | Body JSON                         |
|--------|------------------|----------------------------|------------------------------------|
| GET    | `/careers/`      | List all posts            | —                                  |
| POST   | `/careers/`      | Create a new post         | `{ users.pk, title, content }`     |

### 🔹 Specific Post (`/careers/:pk/`)

| Method | Path                 | Description              | Body JSON             |
|--------|----------------------|---------------------------|------------------------|
| GET    | `/careers/:pk/`     | Retrieve post details     | —                      |
| PUT    | `/careers/:pk/`     | Update post               | `{ title, content }`   |
| DELETE | `/careers/:pk/`     | Delete a post             | —                      |

### 🔹 Post Likes

| Method | Path                            | Description               | Body JSON                       |
|--------|----------------------------------|----------------------------|----------------------------------|
| POST   | `/careers/likes/`                | Add a like to a post       | `{ users.pk, post.pk }`         |
| DELETE | `/careers/likes/{post.pk}/{user.pk}/` | Remove a user's like from a post | —                       |
