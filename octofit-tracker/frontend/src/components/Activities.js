import React, { useEffect, useState } from 'react';

const API_URL = 'https://glorious-memory-97wx779pxr5c7r7w-8000.app.github.dev/api/activity/';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setActivities(data))
      .catch(err => console.error('Error fetching activities:', err));
  }, []);

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-body">
          <h2 className="card-title mb-4">Activities</h2>
          <div className="table-responsive">
            <table className="table table-striped table-hover">
              <thead className="table-dark">
                <tr>
                  <th>Name</th>
                </tr>
              </thead>
              <tbody>
                {activities.map(activity => (
                  <tr key={activity.id}>
                    <td>{activity.name}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Activities;
