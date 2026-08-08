function samples = acquireSamples(sp, count)
%ACQUIRESAMPLES Read up to `count` new integer samples from an open
%serialport object `sp`, skipping comment/header lines (prefixed '#').
%
%   samples = acquireSamples(sp, count)
%
%   sp     - serialport object, already open with configureTerminator(sp,"LF")
%   count  - maximum number of samples to read in this call
%
%   Returns a column vector of samples (may be shorter than `count` if
%   fewer are currently available).
%
% Used by signal_processing/MATLAB/live_radar_pipeline.m and can be reused
% by any other live-acquisition script.

    samples = [];
    n = 0;
    while sp.NumBytesAvailable > 0 && n < count
        line = strtrim(readline(sp));
        if isempty(line) || startsWith(line, "#")
            continue;
        end
        val = str2double(line);
        if ~isnan(val)
            samples(end+1,1) = val; %#ok<AGROW>
            n = n + 1;
        end
    end
end
