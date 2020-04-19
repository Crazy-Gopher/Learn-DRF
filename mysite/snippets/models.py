from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


"""

python manage.py sqlmigrate accounts 0001

## Example 1: Normal Table without (Foreign key and One to One field and Many to Many field)
BEGIN;
--
-- Create model City
--
CREATE TABLE "accounts_city" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(200) NOT NULL, "country" varchar(200) NOT NULL);
--

## Example 2: Foreign key and One to One field(create foreign key constraint and index for foreign key field but does not create index for one to one field)
-- Create model Profile
--
CREATE TABLE "accounts_profile" ("id" serial NOT NULL PRIMARY KEY, "image" varchar(200) NOT NULL, "str_id" varchar(40) NULL, "gender" varchar(1) NULL,
 "birthday" date NULL, "description" text NULL, "new_email" varchar(254) NULL, "is_email_verified" boolean NOT NULL, "mobile" integer NOT NULL,
  "is_mobile_verified" boolean NULL, "last_modified" timestamp with time zone NULL, "order" smallint NOT NULL, "big_field" bigint NOT NULL, 
  "price" numeric(15, 2) NOT NULL, "weight" double precision NULL, "facebook_url" varchar(255) NOT NULL, "city_id" integer NOT NULL, 
  "user_id" integer NOT NULL UNIQUE);
--
ALTER TABLE "accounts_profile" ADD CONSTRAINT "accounts_profile_city_id_267b3d7f_fk_accounts_city_id" FOREIGN KEY ("city_id") 
REFERENCES "accounts_city" ("id") DEFERRABLE INITIALLY DEFERRED;
--
ALTER TABLE "accounts_profile" ADD CONSTRAINT "accounts_profile_user_id_49a85d32_fk_auth_user_id" FOREIGN KEY ("user_id") 
REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
--
CREATE INDEX "accounts_profile_city_id_267b3d7f" ON "accounts_profile" ("city_id");
COMMIT;
"""

"""
python manage.py sqlmigrate snippets 0002
BEGIN;
--
-- Create model Snippet
--
CREATE TABLE "snippets_snippet" ("id" serial NOT NULL PRIMARY KEY, "created" timestamp with time zone NOT NULL, "title" varchar(100) NOT NULL, "code" text NOT NULL, "linenos" boolean NOT NULL, "language" varchar(100) NOT NULL, "style" varchar(100) NOT NULL);
COMMIT;

python manage.py sqlmigrate snippets 0002


--
--  Create model Blog
--
CREATE TABLE "snippets_blog" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "tagline" text NOT NULL);
--
--
## Example 3: Many to many field (create two table and create foreign key contraints , index and unique contraints)
--
-- 1. Create model Author
--
CREATE TABLE "snippets_author" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(200) NOT NULL, "email" varchar(254) NOT NULL);
--
-- 2. Create model Entry
--
CREATE TABLE "snippets_entry" ("id" serial NOT NULL PRIMARY KEY, "headline" varchar(255) NOT NULL, "body_text" text NOT NULL, "pub_date" date NOT NULL, "mod_date" date NOT NULL, "number_of_comments" integer NOT NULL, "number_of_pingbacks" integer NOT NULL, "rating" integer NOT NULL, "blog_id" integer NOT NULL);
ALTER TABLE "snippets_entry" ADD CONSTRAINT "snippets_entry_blog_id_453648b9_fk_snippets_blog_id" FOREIGN KEY ("blog_id") REFERENCES "snippets_blog" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "snippets_entry_blog_id_453648b9" ON "snippets_entry" ("blog_id");
--
-- 3. Create model Author and Entry
--
CREATE TABLE "snippets_entry_authors" ("id" serial NOT NULL PRIMARY KEY, "entry_id" integer NOT NULL, "author_id" integer NOT NULL);
--
ALTER TABLE "snippets_entry_authors" ADD CONSTRAINT "snippets_entry_authors_entry_id_18c195d1_fk_snippets_entry_id" FOREIGN KEY ("entry_id") REFERENCES "snippets_entry" ("id") DEFERRABLE INITIALLY DEFERRED;
--
ALTER TABLE "snippets_entry_authors" ADD CONSTRAINT "snippets_entry_authors_author_id_011fc758_fk_snippets_author_id" FOREIGN KEY ("author_id") REFERENCES "snippets_author" ("id") DEFERRABLE INITIALLY DEFERRED;
--
ALTER TABLE "snippets_entry_authors" ADD CONSTRAINT "snippets_entry_authors_entry_id_author_id_6d870cc5_uniq" UNIQUE ("entry_id", "author_id");
--
CREATE INDEX "snippets_entry_authors_entry_id_18c195d1" ON "snippets_entry_authors" ("entry_id");
CREATE INDEX "snippets_entry_authors_author_id_011fc758" ON "snippets_entry_authors" ("author_id");
COMMIT;

"""
