from typing import List
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


userpost_table = Table(
    "Userpost",
    db.Model.metadata,
    Column("user_id", ForeignKey("user_id")),
    Column("post_id", ForeignKey("post_id")),
)


usercomment_table = Table(
    "Usercomment",
    db.Model.metadata,
    Column("user_id", ForeignKey("user_id")),
    Column("comment_id", ForeignKey("comment_id")),
)

Commentpost_table = Table(
    "Commentpost",
    db.Model.metadata,
    Column("comment_id", ForeignKey("comment_id")),
    Column("post_id", ForeignKey("post_id")),
)

Follower_table = Table(
    "Follower",
    db.Model.metadata,
    Column("user_from_id", ("user_from_id")),
    Column("user_to_id", ("user_to_id")),

)

Media_table = Table(
    "Commentpost",
    db.Model.metadata,
    Column("user_id", ForeignKey("user_id")),
    Column("media_id", ForeignKey("media_id")),
)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    
    User_Post: Mapped[List["Post"]] = relationship(
        "Post",
        secundary =userpost_table,
        back_populates= "Post_by"

    )

    User_Comment: Mapped[List["Post"]] = relationship(
        "Comment",
        secundary =usercomment_table,
        back_populates= "Post_by"

    )

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = Mapped[str] = mapped_column(unique=True, nullable=False)


    def serialize(self) :
        return {
            "id": self.id,
            "user_id": self.user_id
        }

class Comment(db.Model) :
    id:Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column
    author_id: Mapped [int] = mapped_column(unique=True, nullable=False)
    post_id: Mapped[int] = mapped_column(unique=True, nullable=False)

    def serialize(self) :
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id

        }

class Follower(db.Model) :
    user_from_id: Mapped[int] = mapped_column
    user_to_id: Mapped[int] = mapped_column

    def serialize(self):
        return{
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
        }
        
    class Media(db.Model):
        id: Mapped[int] = mapped_column(primary_key=True)
        type: Mapped[str] = mapped_column
        url: Mapped[str] = mapped_column
        post_id: Mapped[int] = mapped_column