import React, { useEffect, useState } from 'react';

const API_URL = 'https://glorious-memory-97wx779pxr5c7r7w-8000.app.github.dev/api/teams/';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setTeams(data))
      .catch(err => console.error('Error fetching teams:', err));
  }, []);

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-body">
          <h2 className="card-title mb-4">Teams</h2>
          <div className="table-responsive">
            <table className="table table-striped table-hover">
              <thead className="table-dark">
                <tr>
                  <th>Name</th>
                  <th>Members</th>
                </tr>
              </thead>
              <tbody>
                {teams.map(team => (
                  <tr key={team.id}>
                    <td>{team.name}</td>
                    <td>{team.members && team.members.length}</td>
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

export default Teams;
