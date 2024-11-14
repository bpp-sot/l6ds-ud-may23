# 1. Insert new project
new_project = {
    "name": "Recommendation Engine",
    "team": ["Sarah", "Michael", "Emma", "David"],
    "technologies": {
        "languages": ["Python", "Scala"],
        "frameworks": ["PySpark", "scikit-learn", "FastAPI"],
        "databases": ["MongoDB", "Redis"]
    },
    "metrics": {
        "precision": 0.89,
        "recall": 0.92,
        "f1_score": 0.90
    },
    "status": "in_progress"
}

# Insert with error handling
success, result = safe_mongodb_operation(
    lambda: collection.insert_one(new_project)
)
if success:
    print(f"Successfully inserted new project with ID: {result.inserted_id}")
else:
    print(f"Error inserting project: {result}")

# 2. Query by technology


def find_projects_by_technology(tech_type, tech_name):
    """
    Find projects using a specific technology
    tech_type can be 'languages', 'frameworks', or 'databases'
    """
    query = {f"technologies.{tech_type}": tech_name}
    try:
        projects = collection.find(query)
        print(f"\nProjects using {tech_name}:")
        for project in projects:
            print(f"- {project['name']}")
            print(f"  Team: {', '.join(project['team'])}")
            print(f"  Status: {project['status']}")
    except Exception as e:
        print(f"Error querying projects: {e}")


# Example usage
find_projects_by_technology("frameworks", "scikit-learn")
find_projects_by_technology("languages", "Python")

# 3. Aggregation pipeline to find most common programming language
pipeline = [
    # Unwind the languages array
    {"$unwind": "$technologies.languages"},

    # Group by language and count occurrences
    {
        "$group": {
            "_id": "$technologies.languages",
            "count": {"$sum": 1},
            "projects": {"$push": "$name"}
        }
    },

    # Sort by count in descending order
    {"$sort": {"count": -1}},

    # Limit to top 5 languages
    {"$limit": 5}
]

# Execute aggregation with error handling
success, result = safe_mongodb_operation(
    lambda: list(collection.aggregate(pipeline))
)

if success:
    print("\nMost common programming languages:")
    for lang_data in result:
        print(f"\n{lang_data['_id']}:")
        print(f"Used in {lang_data['count']} projects:")
        for project in lang_data['projects']:
            print(f"- {project}")
else:
    print(f"Error in aggregation: {result}")

# 4. Update project metrics with error handling


def update_project_metrics(project_name, new_metrics):
    """
    Update a project's metrics with error handling

    Args:
        project_name (str): Name of the project to update
        new_metrics (dict): Dictionary containing new metric values
    """
    try:
        # First check if project exists
        project = collection.find_one({"name": project_name})
        if not project:
            raise ValueError(f"Project '{project_name}' not found")

        # Validate metrics
        required_metrics = ["precision", "recall", "f1_score"]
        for metric in required_metrics:
            if metric not in new_metrics:
                raise ValueError(f"Missing required metric: {metric}")
            if not isinstance(new_metrics[metric], (int, float)):
                raise ValueError(f"Metric {metric} must be a number")
            if not 0 <= new_metrics[metric] <= 1:
                raise ValueError(f"Metric {metric} must be between 0 and 1")

        # Update metrics
        result = collection.update_one(
            {"name": project_name},
            {"$set": {"metrics": new_metrics}}
        )

        if result.modified_count > 0:
            print(f"Successfully updated metrics for '{project_name}'")
        else:
            print(f"No changes made to '{project_name}'")

        # Fetch and display updated project
        updated_project = collection.find_one({"name": project_name})
        print("\nUpdated project metrics:")
        pprint(updated_project['metrics'])

    except Exception as e:
        print(f"Error updating metrics: {e}")


# Example usage of update_project_metrics
new_metrics = {
    "precision": 0.95,
    "recall": 0.88,
    "f1_score": 0.91
}

update_project_metrics("Recommendation Engine", new_metrics)

# Test error handling with invalid metrics
invalid_metrics = {
    "precision": 1.5,  # Invalid value > 1
    "recall": 0.88
    # Missing f1_score
}

update_project_metrics("Recommendation Engine", invalid_metrics)
