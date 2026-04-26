// A utility to clean and format incoming JSON data for business applications
const formatClientData = (rawData) => {
    return rawData.map(user => {
        return {
            id: user.id,
            fullName: `${user.firstName} ${user.lastName}`,
            activeStatus: user.lastLogin ? 'Active' : 'Inactive',
            verified: true
        };
    });
};

console.log("Data Formatting Engine: Ready");
