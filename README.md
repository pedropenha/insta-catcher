# Instagram image catcher

## How to work

in the variable profile change the username to the username of the profile from which you want to download the images.
``` python

profile = Profile.from_username(L.context, username="username to get the images")

```

After modifying the profile, it will be necessary to include the hashtag that you want to search in the user's profile.

```python
hashtag1 = '#marcenariasobmedida'
hashtag2 = 'marcenariasobmedida'
```

Done, now just run the file that your images are saved in the root of your directory.

## References
To find out more about how the instaloader api works, you can access the documentation through this link

https://instaloader.github.io/