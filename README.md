# Onboarding Tracker System

A comprehensive HR onboarding tracking system with role-based access control.

## Features

- **Three User Roles**: Admin, Editor, Viewer
- **Candidate Management**: Track candidates through hiring process
- **Vacancy Management**: Manage job vacancies
- **Analytics Dashboard**: Charts and reports
- **Email Integration**: Send emails to candidates
- **Export Functionality**: Export data to Excel/CSV
- **Local Storage**: Works offline with localStorage

## Login Credentials

| Role | Email | Password |
|------|-------|----------|
| Admin | hr.jpr@grew.one | Ankit@0708 |
| Editor | rakesh.s@grew.one | Rakesh@1234 |
| Viewer | View@gmail.com | View@1234 |

## File Structure

- `index.html` - Login page
- `dashboard.html` - Main application
- `supabase_schema.sql` - Database schema for Supabase
- `hash_passwords.py` - Password hashing utility

## Setup Instructions

### 1. Local Usage
Simply open `index.html` in your web browser. No server required.

### 2. Supabase Integration (Optional)
1. Create a Supabase account
2. Run the SQL from `supabase_schema.sql` in the SQL Editor
3. Update the JavaScript in `dashboard.html` to use Supabase API

### 3. Deployment
Deploy to any static hosting service:
- GitHub Pages
- Netlify
- Vercel
- Firebase Hosting

## Technologies Used

- HTML5, CSS3, JavaScript (ES6+)
- Chart.js for analytics
- Font Awesome for icons
- Google Fonts (Poppins)
- localStorage for data persistence

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 10+
- Edge 79+

## Security Notes

- Passwords are stored in plaintext in localStorage (for demo only)
- In production, use proper authentication with hashed passwords
- Enable HTTPS for production deployment
- Implement proper input validation

## License

MIT License - Free for commercial and personal use.
