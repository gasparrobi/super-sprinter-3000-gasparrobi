from flask import Flask, render_template, request, redirect, url_for
from models import *
from AppFunctions import *


app = Flask(__name__)

"""GLOBAL PERMANENT VARIABLES USED FOR MORE THAN 1 ROUTES """
value_options = AppFunctions.generate_value_options()
len_v_options = len(value_options)
estimate_options = AppFunctions.generate_estimation_options()
len_e_options = len(estimate_options)


@app.route("/list")
@app.route("/", methods=["GET", "POST"])
def index():
    stories = UserStoryManager.select()
    return render_template("list.html", stories=stories)


@app.route("/story", methods=["GET", "POST"])
def new_user_story(new=True):
    if request.method == "GET":
        return render_template("form.html",
                               new=new,
                               value_options=value_options,
                               estimate_options=estimate_options,
                               len_e_options=len_e_options,
                               len_v_options=len_v_options)
    else:
        UserStoryManager.create(title=request.form.get('storytitle'),
                                story=request.form.get('userstory'),
                                criteria=request.form.get('criteria'),
                                value=request.form.get('value'),
                                estimation=request.form.get('estimation'),
                                status=request.form.get('status'))
        return redirect(url_for("index"))


@app.route("/edit_story/<story_id>", methods=["GET", "POST"])
def edit_user_story(story_id, new=False):
    story = UserStoryManager.select().where(UserStoryManager.id == story_id).get()
    if request.method == "GET":
        return render_template("form.html",
                               story=story,
                               new=new,
                               value_options=value_options,
                               estimate_options=estimate_options,
                               len_e_options=len_e_options,
                               len_v_options=len_v_options)
    else:
        story.title = request.form.get('storytitle')
        story.story = request.form.get('userstory')
        story.criteria = request.form.get('criteria')
        story.value = request.form.get('value')
        story.estimation = request.form.get('estimation')
        story.status = request.form.get('status')
        story.save()
        return redirect(url_for("index"))


@app.route("/delete/<story_id>")
def delete_story(story_id):
    try:
        story = UserStoryManager.delete().where(UserStoryManager.id == story_id)
        story.execute()
        return redirect(url_for("index"))
    except Exception:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)