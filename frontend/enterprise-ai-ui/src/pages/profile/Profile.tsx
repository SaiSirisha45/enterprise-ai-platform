export default function Profile() {
  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div>
        <h1 className="text-3xl font-bold dark:text-white">
          My Profile
        </h1>

        <p className="text-gray-500 dark:text-gray-400">
          Manage your profile information
        </p>
      </div>

      {/* Profile Card */}
      <div className="rounded-xl bg-white p-8 shadow dark:bg-gray-800">
        <div className="flex flex-col items-center md:flex-row md:items-start md:gap-8">
          {/* Avatar */}
          <div className="flex h-32 w-32 items-center justify-center rounded-full bg-blue-600 text-4xl font-bold text-white">
            SS
          </div>

          {/* User Details */}
          <div className="mt-6 flex-1 md:mt-0">
            <div className="grid gap-6 md:grid-cols-2">

              <div>
                <label className="text-sm text-gray-500">
                  Full Name
                </label>

                <p className="text-lg font-semibold dark:text-white">
                  Sai Sirisha
                </p>
              </div>

              <div>
                <label className="text-sm text-gray-500">
                  Email
                </label>

                <p className="text-lg dark:text-white">
                  demo@company.com
                </p>
              </div>

              <div>
                <label className="text-sm text-gray-500">
                  Role
                </label>

                <p className="text-lg dark:text-white">
                  Enterprise AI Engineer
                </p>
              </div>

              <div>
                <label className="text-sm text-gray-500">
                  Department
                </label>

                <p className="text-lg dark:text-white">
                  Artificial Intelligence
                </p>
              </div>

              <div>
                <label className="text-sm text-gray-500">
                  Phone
                </label>

                <p className="text-lg dark:text-white">
                  +91 98765 43210
                </p>
              </div>

              <div>
                <label className="text-sm text-gray-500">
                  Location
                </label>

                <p className="text-lg dark:text-white">
                  Hyderabad, India
                </p>
              </div>

            </div>

            <button className="mt-8 rounded-lg bg-blue-600 px-6 py-3 text-white hover:bg-blue-700">
              Edit Profile
            </button>
          </div>
        </div>
      </div>
    </div>
  );
} 