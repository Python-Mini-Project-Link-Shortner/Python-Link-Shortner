from flask  import (
    render_template, 
    url_for, request, 
    redirect, jsonify, 
    Blueprint
    )
from app    import create_app

app = create_app()

if __name__ == "__main__":
    print(app.root_path)
    print(app.static_folder)
    print(app.static_url_path)
    print(app._static_folder)
    app.run(debug=True)