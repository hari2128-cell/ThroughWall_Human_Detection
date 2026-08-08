%% tuneThreshold.m
% Sweeps a range of energy thresholds against a labeled set of recordings
% (static vs. human motion) and reports precision/recall/F1 for each, to
% help pick a good operating threshold for detectMotion.m.
%
% Expects labeled CSVs in datasets/Labeled/ with filenames indicating the
% true class, e.g. "static_*.csv" and "motion_*.csv". Adjust the glob
% patterns below to match your actual dataset filenames.

function tuneThreshold(labeledDir, Fs)
    if nargin < 1, labeledDir = fullfile('..','..','datasets','Labeled'); end
    if nargin < 2, Fs = 1000; end

    staticFiles = dir(fullfile(labeledDir, 'static_*.csv'));
    motionFiles = dir(fullfile(labeledDir, 'motion_*.csv'));

    if isempty(staticFiles) || isempty(motionFiles)
        warning(['No labeled files found matching static_*.csv / motion_*.csv in %s.\n' ...
                 'Populate datasets/Labeled/ (see its README) before running this script.'], labeledDir);
        return;
    end

    staticEnergies = computeEnergies(staticFiles, labeledDir, Fs);
    motionEnergies = computeEnergies(motionFiles, labeledDir, Fs);

    thresholds = linspace(0, max([staticEnergies; motionEnergies]), 50);
    fprintf('%10s %10s %10s %10s\n', 'Thresh', 'Precision', 'Recall', 'F1');

    for t = thresholds
        tp = sum(motionEnergies > t);
        fn = sum(motionEnergies <= t);
        fp = sum(staticEnergies > t);
        precision = tp / max(tp + fp, 1);
        recall = tp / max(tp + fn, 1);
        f1 = 2 * precision * recall / max(precision + recall, eps);
        fprintf('%10.3f %10.3f %10.3f %10.3f\n', t, precision, recall, f1);
    end
end

function energies = computeEnergies(files, dirPath, Fs)
    energies = zeros(numel(files), 1);
    for i = 1:numel(files)
        x = readmatrix(fullfile(dirPath, files(i).name));
        x = x(:,1) - mean(x(:,1));
        [b, a] = butter(4, [0.5 40] / (Fs/2), 'bandpass');
        xf = filtfilt(b, a, x);
        N = numel(xf);
        X = fft(xf .* hann(N));
        mag = abs(X(1:floor(N/2))) / N;
        energies(i) = sum(mag.^2);
    end
end
