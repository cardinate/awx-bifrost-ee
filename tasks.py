from invoke import task


@task
def build_ee(c):
    """Builds the container image for awx-bifrost-ee with a verbose debug"""
    c.run("ansible-builder build -t awx-bifrost-ee:latest -v 3")


@task
def create_ee(c):
    """Optionally creates the file structure for the ee so you can manully inspect it"""
    c.run("ansible-builder create")
